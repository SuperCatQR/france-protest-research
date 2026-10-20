$src = 'C:\WorkSpace\调查研究\报告\02_国家回应_政治反应与处置手段.md'
$patch = 'C:\WorkSpace\调查研究\核查报告\patches\P2_02.md'
$t = [System.IO.File]::ReadAllText($src)
$pl = [System.IO.File]::ReadAllLines($patch)

$blocks = New-Object System.Collections.ArrayList
$cur = $null
foreach ($line in $pl) {
    if ($line.StartsWith('- **原文**')) {
        if ($cur -ne $null) { [void]$blocks.Add(($cur -join "`n")) }
        $cur = New-Object System.Collections.ArrayList
    }
    elseif ($line.StartsWith('  > ')) {
        if ($cur -ne $null) { [void]$cur.Add($line.Substring(4)) }
    }
    elseif ($line.StartsWith('  >')) {
        if ($cur -ne $null) { [void]$cur.Add('') }
    }
    elseif ($cur -ne $null -and $line -notlike '  >*' -and $line.Trim() -ne '') {
        [void]$blocks.Add(($cur -join "`n"))
        $cur = $null
    }
}
if ($cur -ne $null) { [void]$blocks.Add(($cur -join "`n")) }

Write-Output "original blocks parsed: $($blocks.Count)"
$ok = 0
foreach ($b in $blocks) {
    $n = 0; $i = 0
    while (($i = $t.IndexOf($b, $i)) -ge 0) { $n++; $i += $b.Length }
    if ($n -eq 1) { $ok++ }
    else {
        Write-Output ("--- count=$n ---")
        Write-Output $b
    }
}
Write-Output "verbatim and unique: $ok / $($blocks.Count)"

# anchor uniqueness
$anchors = $pl | Where-Object { $_.StartsWith('- **定位锚点**') }
Write-Output "anchor lines: $($anchors.Count)"
