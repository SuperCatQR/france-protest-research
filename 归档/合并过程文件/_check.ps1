# 校验合并报告的 URL 完整性与内容保真度
# 成品在 报告/，合并前原文在 归档/原始七份报告合并前/
# 报告 04 另并入了 docs/报告/ 下两份 USL／FIDL 专题底稿，其源文来自那里，故单独标注 Docs
# （《高中封锁期_组织者归因核实》未并入 报告/04，不进本校验）
param(
    [string]$Root = (Split-Path (Split-Path $PSScriptRoot -Parent) -Parent)
)

$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new()

$targets = @(
    @{ Out = '01_事件本体_人员构成与时间线.md'; Src = @('01_事件人员构成.md','02_事件时间线.md'); MinRatio = 0.85 },
    @{ Out = '02_国家回应_政治反应与处置手段.md'; Src = @('03_法国国内政治反应.md','06_政府处置案例.md'); MinRatio = 0.85 },
    @{ Out = '03_历史脉络_近年类似事件与关联.md'; Src = @('04_与近年事件的脉络.md','05_近年类似事件基本情况.md'); MinRatio = 0.85 },
    @{ Out = '04_组织动员_高中生组织与行动方式.md'; Src = @('07_高中生组织与行动方式.md'); MinRatio = 0.85
       Docs = @('USL与FIDL_规模与代表性核实.md','USL与FIDL_诉求与纲领对照.md') }
)

function Get-Urls([string]$path) {
    if (-not (Test-Path -LiteralPath $path)) { return @() }
    $t = Get-Content -LiteralPath $path -Raw -Encoding UTF8
    [regex]::Matches($t, 'https?://[^\s\)\]\>]+') |
        ForEach-Object { $_.Value.TrimEnd('.', ',', ';') } |
        Sort-Object -Unique
}

$fail = 0
foreach ($t in $targets) {
    $outPath = Join-Path $Root "报告\$($t.Out)"
    Write-Host ""
    Write-Host ("=" * 78)
    Write-Host "输出: $($t.Out)"
    if (-not (Test-Path -LiteralPath $outPath)) {
        Write-Host "  [FAIL] 文件不存在" -ForegroundColor Red
        $fail++
        continue
    }

    $srcUrls = @()
    $srcChars = 0
    foreach ($s in $t.Src) {
        $sp = Join-Path $Root "归档\原始七份报告合并前\$s"
        $srcUrls += Get-Urls $sp
        if (Test-Path -LiteralPath $sp) {
            $srcChars += (Get-Content -LiteralPath $sp -Raw -Encoding UTF8).Length
        }
    }
    if ($t.Docs) {
        foreach ($s in $t.Docs) {
            $sp = Join-Path $Root "docs\报告\$s"
            $srcUrls += Get-Urls $sp
            if (Test-Path -LiteralPath $sp) {
                $srcChars += (Get-Content -LiteralPath $sp -Raw -Encoding UTF8).Length
            }
        }
    }
    $srcUrls = $srcUrls | Sort-Object -Unique

    $outText = Get-Content -LiteralPath $outPath -Raw -Encoding UTF8
    $outUrls = Get-Urls $outPath
    $outChars = $outText.Length
    $outLines = ($outText -split "`n").Count

    $missing = @($srcUrls | Where-Object { $outUrls -notcontains $_ })
    $extra   = @($outUrls | Where-Object { $srcUrls -notcontains $_ })
    $ratio   = if ($srcChars -gt 0) { $outChars / $srcChars } else { 0 }

    Write-Host ("  行数 {0}  字符 {1} / 源 {2}  保真率 {3:P1}  (下限 {4:P0})" -f `
        $outLines, $outChars, $srcChars, $ratio, $t.MinRatio)
    Write-Host ("  源 URL {0}  输出 URL {1}  缺失 {2}  新增 {3}" -f `
        $srcUrls.Count, $outUrls.Count, $missing.Count, $extra.Count)

    if ($missing.Count -gt 0) {
        Write-Host "  [FAIL] 丢失 URL:" -ForegroundColor Red
        $missing | ForEach-Object { Write-Host "    - $_" -ForegroundColor Red }
        $fail++
    }
    if ($extra.Count -gt 0) {
        Write-Host "  [WARN] 新增 URL（源中不存在，可能是补链）:" -ForegroundColor Yellow
        $extra | ForEach-Object { Write-Host "    + $_" -ForegroundColor Yellow }
        $fail++
    }
    if ($ratio -lt $t.MinRatio) {
        Write-Host "  [FAIL] 内容缩水超过允许范围" -ForegroundColor Red
        $fail++
    }
    if ($missing.Count -eq 0 -and $extra.Count -eq 0 -and $ratio -ge $t.MinRatio) {
        Write-Host "  [PASS]" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host ("=" * 78)
if ($fail -eq 0) { Write-Host "全部通过" -ForegroundColor Green }
else { Write-Host "存在 $fail 项问题" -ForegroundColor Red }
exit $fail
