import csv
import os
import termcolor

first_contact = termcolor.colored('#' * 50 + '\n\nこんにちは！私はRobokoです。あなたの名前はなんですか？\n\n' + '#' * 50, 'green')

print(first_contact)
name = input().title()

if os.path.exists('ranking.csv'):
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            other_contact = termcolor.colored('#' * 50 + '\n\n私のオススメのレストランは{}です。\n\nこのレストランは好きですか？ [Yes/No]\n\n'.format(row['Name']) + '#' * 50, 'green')
            print(other_contact)
            answer = input()
            if answer.lower() == 'y' or answer.lower() == 'yes':
                break
else:
    with open('ranking.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

second_contact = termcolor.colored('#' * 50 + '\n\n{}さん。どこのレストランが好きですか？\n\n'.format(name) + '#' * 50, 'green')

print(second_contact)
restaurant = input().title()

last_contact = termcolor.colored('#' * 50 + '\n\n{}さん。ありがとうございました。\n\n良い一日を！さようなら。\n\n'.format(name) + '#' * 50, 'green')
print(last_contact)

if os.path.exists('ranking.csv'):
    with open('ranking.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['{}'.format(restaurant), 1])
