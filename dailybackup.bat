set time=%time%
set Y=%date:~0,4%
set N=%date:~5,2%
set D=%date:~8,2%
set h=%time:~0,2%
set m=%time:~3,2%
set s=%time:~6,2%
set dailybackup=D:\dailybackup
set daysago=15

@echo off
cd D:\
if not exist %dailybackup% (md D:\dailybackup) else (echo 文件夹已存在)
C:\cwrsync\bin\rsync -avzbP --bwlimit=4096 --suffix="_%Y%%N%%D%-%h%%m%%s%" --exclude-from=/cygdrive/c/excluded.txt /cygdrive/D/ /cygdrive/D/dailybackup/%Y%%N%%D%
echo ERRORLEVEL==%errorlevel% 
forfiles /p %dailybackup% /d -%daysago% /c "cmd /c if @isdir == TRUE rd /s /q @path"