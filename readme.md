# Image social app

## Reference

* Mele, J. 예제로 배우는 Django 4
  * Chapter 4 through 7
    4. 소셜 웹사이트 구축하기
    5. 소셜 인증 구현하기
    6. 웹사이트에서 콘텐츠 공유하기
    7. 사용자 활동 추적하기

## Structure

* [bookmarks](/bookmarks/): Django Project
  * [account](/bookmarks/account/): app for account, auth
  * [bookmarks](/bookmarks/bookmarks/): project settings
  * [images](/bookmarks/images/): app for image upload and social interactions (main business logic)  
  * [actions](/bookmarks/actions/): app for making user stream, powered by Redis (running docker container needed)
* [venv](/venv/): Python Virtual Environment
  * Powershell `.\venv\Script\activate`
  * Bash: load with `source venv/Script/activate`
  * unload with `deactivate`
* [readme](/readme.md): this markdown file
* [requirements.txt](/requirements.txt): Python dependency
  * load with `pip install -r requirements.txt`
  * write with `pip freeze > requirements.txt`
  