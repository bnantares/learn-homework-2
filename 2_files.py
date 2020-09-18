"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as myfile:
        words = 0       
        content = myfile.read()
        content_length = len(content)
        print(f"Длина строки: {content_length} символов.")

    with open('referat.txt', 'r', encoding='utf-8') as myfile:    
        for line in myfile:
            wordslist=line.split()
            words += len(wordslist)
    print(f"В тексте {words} слов")

    with open('referat.txt', 'r', encoding="utf-8") as myfile, open('referat2.txt', 'w', encoding="utf-8") as myfile2:
        for line in myfile:
            line = line.replace('.', '!')
            myfile2.write(line)        
            
    

if __name__ == "__main__":
    main()
