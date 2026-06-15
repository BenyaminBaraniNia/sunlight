# ☀️ Sunlight

Everything is visible under the sunlight.

**Sunlight** is a simple tool for analyzing Instagram exported data.  
Put your Instagram files next to Sunlight, run it, and it will create clean result files for you.

## ✨ Features

- 👀 Find people you follow who do not follow you back
- 🤝 Find people who follow you, but you do not follow back
- 📩 Extract recent follow requests
- 📊 Create basic page statistics
- 🔗 Generate Instagram profile links

## 🔒 Security

Sunlight does **not** send, upload, or share your data with anyone or anywhere.

Everything happens locally on your own computer.  
Your Instagram files stay on your computer, and the result files are created in the same folder as Sunlight.

## 📥 How To Export Instagram Data

1. Open Instagram.
2. Go to your profile.
3. Open the menu.
4. Go to **Accounts Center**.
5. Open **Your information and permissions**.
6. Choose **Download your information**.
7. Select your Instagram account.
8. Choose the information related to followers and following.
9. Select **JSON** format.
10. Create the export request.
11. Download the file when Instagram prepares it.
12. Extract the downloaded ZIP file.
13. Find these files and place them next to Sunlight:

```text
followers_1.json
following.json
recent_follow_requests.json
```

## 🚀 How To Use EXE Version

1. Put `Sunlight.exe` in a folder.
2. Put your Instagram JSON files in the same folder.
3. Double-click `Sunlight.exe`.
4. Wait until the result files are created.

## 🐍 How To Use Source Code Version

If you prefer to run the source code directly:

1. Install Python.
2. Download or clone this repository.
3. Put your Instagram JSON files in the same folder as `sunlight.py`.
4. Run this command:

```bash
python sunlight.py
```

## 📄 Output Files

Sunlight creates these files:

```text
01-Page_Statistics.txt
02-Not_Following_You_Back.txt
03-Not_Following_You_Back_Links.txt
04-You_Do_Not_Follow_Back.txt
05-You_Do_Not_Follow_Back_Links.txt
06-Recent_Follow_Requests.txt
07-Recent_Follow_Requests_Links.txt
```

## 📊 Statistics

`01-Page_Statistics.txt` shows a quick summary:

```text
Followers: 1200
Following: 900
Not following you back: 150
You do not follow back: 300
Recent follow requests: 5
```

## 🛠️ Reporting Issues

If you find a bug or have a problem, please open an issue in this GitHub repository or send me an email.

Please include:

- What happened
- What you expected to happen
- A screenshot of the error, if possible
- Which file caused the problem, if you know it

Please do **not** share private Instagram data publicly.  
Remove usernames or personal information before sending examples.

## 📬 Contact Me

- Email: [Benyamin.Barani.Nia@gmail.com](mailto:Benyamin.Barani.Nia@gmail.com)
- Website: [BenWrites.ir](https://www.BenWrites.ir/)
- GitHub: [BenyaminBaraniNia](https://github.com/BenyaminBaraniNia)
- Instagram: [@benyamin.b.n](https://www.instagram.com/benyamin.b.n/)
- Telegram Channel: [@benyaminwrites](https://t.me/benyaminwrites)

## 💡 Notes

Sunlight uses `utf-8` encoding to better support Persian, Arabic, emojis, and special characters.
