[CmdletBinding()]
param(
    [switch]$Json,
    [string]$ShortName,
    [int]$Number = 0,
    [switch]$Help,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$FeatureDescription
)

$repoRoot = "D:\TODO\Todo_Phase_1"
$branchName = "001-todo-console-app"
$promptsDir = "$repoRoot\history\prompts\$branchName"
New-Item -ItemType Directory -Path $promptsDir -Force | Out-Null
