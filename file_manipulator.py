import os
import sys

#パスのバリデーション
def inputCheck(path):
    #バリデーション用のリスト
    validateList = ["<", ">",":",'"', "\\", "|", "?", "*"]
    if path == "":
            return False
    #OSごとの条件分岐
    osName = os.name
    if osName == "posix": #macかlinux
        for char in path:
            if char in validateList :
                print("無効な文字が入っています。")
                return False
    elif osName == "nt": #windows
        tempList = validateList.copy()
        tempList.remove(":")
        for char in path:
            if char in tempList :
                print("無効な文字が入っています。")
                return False
    else:   
        print("未知のOSが使われています。システムの対応外です。")
        return False 
   
    #パスであるかチェック
    if path.startswith("/") or path.startswith(".")or (len(path)>1 and path[1] == ":" and path[0].isalpha()):
        return True
    else:
        print("パスの形式が不正です。")
        return False

def reverse(inputPath,outputPath):
    
    if not inputCheck(outputpath):
        sys.exit("出力パスを正しいものに変えてやり直してください。")
    if not inputCheck(inputpath):
        sys.exit("入力パスを正しいものに変えてやり直してください。")
    else:  
        print('対象のファイルがあるか検索します。')
    if os.path.exists(inputpath) == True:
        with open(inputpath) as f:
            fileContent = f.read()
            print("ファイルが見つかりました。")
    else:
        sys.exit("ファイルがありませんでした、終了します。")

    outPutContent = ''

    for char in reversed(fileContent):
        outPutContent += char
    with open(outputpath,'w') as f2:
        f2.write(outPutContent)

def copy(inputpath,outputpath):
    
    if not inputCheck(outputpath):
        sys.exit("出力パスを正しいものに変えてやり直してください。")
    if not inputCheck(inputpath):
        sys.exit("入力パスを正しいものに変えてやり直してください。")
    else:  
        print('対象のファイルがあるか検索します。')
    if os.path.exists(inputpath) == True:
        with open(inputpath) as f:
            fileContent = f.read()
            print("ファイルが見つかりました。")
    else:
        sys.exit("ファイルがありませんでした、終了します。")

    outPutContent = ''

    for char in fileContent:
        outPutContent += char
    with open(outputpath,'w') as f2:
        f2.write(outPutContent)

def duplicate_contents(inputpath,n):
    if not n.isdigit():
        sys.exit("コピー回数に数字を入れてください。")
    if not inputCheck(inputpath):
        sys.exit("入力パスを正しいものに変えてやり直してください。")
    else:  
        print('対象のファイルがあるか検索します。')
    if os.path.exists(inputpath) == True:
        with open(inputpath) as f:
            fileContent = f.read()
            print("対象のファイルが見つかりました。")
    else:
        sys.exit("対象のファイルがありませんでした、終了します。")

    outPutContent = ''

    for a in range(int(n)):
        outPutContent += fileContent
    with open(inputpath,'a') as f2:
        f2.write(outPutContent)

def replace_string(inputpath,serchString,replaceString):
    if os.path.exists(inputpath) == True:
        with open(inputpath) as f:
            fileContent = f.read()
            print("対象のファイルが見つかりました。")
    else:
        sys.exit("対象のファイルがありませんでした、終了します。")

    if serchString in fileContent:
        outPutContent = fileContent.replace(serchString,replaceString)
    else:
        sys.exit("置換する文字列がありません終了します。")
    with open(inputpath,'w') as f2:
        f2.write(outPutContent)


inputData = input().split()
if inputData[0] == "reverse":
    reverse(inputData[1],inputData[2])
elif inputData[0] == "copy":
    copy(inputData[1],inputData[2])

elif inputData[0] == "duplicate-contents":
    duplicate_contents(inputData[1],inputData[2])
elif inputData[0] == "replace-string":
     replace_string(inputData[1],inputData[2],inputData[3])

print("finish!!")






    
    
