from appointment import appointment, db, User

# Create an application context
with appointment.appointment_context():
    # Create the database tables (if they don't exist)
    db.create_all()

    # Add a sample user
    sample_user = User(
        email='sample@example.com',
        security_question='What is your mother\'s maiden name?',
        security_answer='SampleAnswer',
        password='SamplePassword'
    )
    db.session.add(sample_user)
    db.session.commit()

    print("Sample user added successfully!")
