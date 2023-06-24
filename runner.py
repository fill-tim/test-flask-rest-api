from app import application, db

if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    application.run()
