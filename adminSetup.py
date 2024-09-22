from app import app, db, User

# Create an admin user
with app.app_context():
    # Check if the admin user already exists
    if User.query.filter_by(email='admin@example.com').first() is None:
        admin_user = User(
            first_name='Admin1',
            last_name='User',
            email='admin1@example.com',
            phone='1234567890',
            address='Admin Address'
        )
        admin_user.set_password('Test123')  # Set the admin password
        admin_user.is_admin = True  # Set the user as admin

        # Add and commit the user to the database
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")
