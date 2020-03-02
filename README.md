# Pic Hub

### As users you can :
* View different photos that interest me.
* View different categories of photos.
* Copy a link to the photo to share with my friends.
***

***## ~~Usage example~~

1. Open the website and browse the images.
2. If you see an image that interests you you can click on it to view it.***


## Development setup

- To access the Code behind this site, you will need to:

1. Clone this repo:
  ```bash
  git clone https://github.com/brayooh/gallery
  ```
2. Move to the folder and install requirements
  ```bash
  cd gallery
  pip install -r requirements.txt
  ```
3. Create database on psql shell
  ```SQL
  psql
  CREATE DATABASE dbgallery;
  ```
4. Migrate the database and run the application
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

## Technologies Used
* python3.6
* Django3
* HTML5
* Bootstrap4
* CSS3


## Known Bugs.
* There are currently no known bugs. Feel free to open an issue concerning the app anytime :)

## Support and contact details
If you have any queries regarding the app, Please feel free to
contact the developer team on [gmail](brianndichu.bn@gmail.com) and I will be ready to respond.

### Licence
[MIT](LICENSE)




