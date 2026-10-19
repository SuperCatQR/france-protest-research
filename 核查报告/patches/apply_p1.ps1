# 将 P1 补丁片段应用到报告文件
# 规则：每块必须「定位锚点唯一」且「原文逐字匹配」，否则拒绝应用并报告

$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new()
$Root = "C:\WorkSpace\调查研究"
$PatchDir = "$Root\核查报告\patches"

$targets = @(
    @{ Id = '01'; File = "$Root\报告\01_事件本体_人员构成与时间线.md" },
    @{ Id = '02'; File = "$Root\报告\02_国家回应_政治反应与处置手段.md" },
    @{ Id = '03'; File = "$Root\报告\03_历史脉络_近年类似事件与关联.md" },
    @{ Id = '04'; File = "$Root\报告\04_组织动员_高中生组织与行动方式.md" }
)

function Get-Urls([string]$t) {
    [regex]::Matches($t, 'https?://[^\s\)\]\>]+') | ForEach-Object { $_.Value.TrimEnd('.', ',', ';') } | Sort-Object -Unique
}

$summary = @()

foreach ($t in $targets) {
    $patchFile = "$PatchDir\P1_$($t.Id).md"
    if (-not (Test-Path -LiteralPath $patchFile)) {
        $summary += "  [$($t.Id)] 补丁文件不存在，跳过"
        continue
    }

    $doc = Get-Content -LiteralPath $t.File -Raw -Encoding UTF8
    $urlsBefore = Get-Urls $doc
    $patch = Get-Content -LiteralPath $patchFile -Raw -Encoding UTF8

    # 解析块：### 标题 / 原文引用块 / 改为引用块
    $blocks = [regex]::Matches($patch, '(?ms)^### (.+?)$(.*?)(?=^### |\z)')
    $applied = 0; $skipped = 0; $failed = @()

    foreach ($b in $blocks) {
        $title = $b.Groups[1].Value.Trim()
        $body = $b.Groups[2].Value

        if ($body -match '结论\*\*：无需改动') { $skipped++; continue }
        if ($body -match '结论\*\*：无法处理') { $skipped++; continue }

        # 取「原文」块
        $mOld = [regex]::Match($body, '(?ms)-\s*\*\*原文\*\*[^\n]*\n(.*?)(?=\n-\s*\*\*改为)')
        $mNew = [regex]::Match($body, '(?ms)-\s*\*\*改为\*\*[^\n]*\n(.*?)(?=\n-\s*\*\*|\z)')
        if (-not $mOld.Success -or -not $mNew.Success) { $failed += "$title : 解析失败"; continue }

        $oldText = ($mOld.Groups[1].Value -split "`n" | ForEach-Object { $_ -replace '^\s*>\s?', '' }) -join "`n"
        $newText = ($mNew.Groups[1].Value -split "`n" | ForEach-Object { $_ -replace '^\s*>\s?', '' }) -join "`n"
        $oldText = $oldText.TrimEnd(); $newText = $newText.TrimEnd()
        if ([string]::IsNullOrWhiteSpace($oldText)) { $failed += "$title : 原文为空"; continue }

        # 匹配检验
        $idx = $doc.IndexOf($oldText)
        if ($idx -lt 0) { $failed += "$title : 原文不匹配"; continue }
        $second = $doc.IndexOf($oldText, $idx + 1)
        if ($second -ge 0) { $failed += "$title : 原文出现多次（不唯一）"; continue }

        $doc = $doc.Substring(0, $idx) + $newText + $doc.Substring($idx + $oldText.Length)
        $applied++
    }

    $urlsAfter = Get-Urls $doc
    $miss = @($urlsBefore | Where-Object { $urlsAfter -notcontains $_ })
    $extra = @($urlsAfter | Where-Object { $urlsBefore -notcontains $_ })

    if ($miss.Count -eq 0 -and $extra.Count -eq 0 -and $failed.Count -eq 0) {
        Set-Content -LiteralPath $t.File -Value $doc -Encoding UTF8 -NoNewline
        $summary += "  [$($t.Id)] 应用 $applied 块，跳过 $skipped，URL $($urlsBefore.Count)→$($urlsAfter.Count) OK"
    }
    else {
        $summary += "  [$($t.Id)] **未写入**：应用 $applied，失败 $($failed.Count)，URL 缺 $($miss.Count) 增 $($extra.Count)"
        $failed | ForEach-Object { $summary += "      × $_" }
        $miss | Select-Object -First 5 | ForEach-Object { $summary += "      - 缺 $_" }
        $extra | Select-Object -First 5 | ForEach-Object { $summary += "      + 增 $_" }
    }
}

$summary | ForEach-Object { Write-Host $_ }
