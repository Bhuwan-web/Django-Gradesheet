# IW Bootcamp final Project

    This is the project made as a capstone project for the IW workshop I enrolled.
    Due to the busy schedule and festival season i wasn't able to complete whole project but the basic design of the project has been completed.
    The main and extrime challange as a beginner i faced was to make the complex design where
    different users with different roles has different inputs to make and different outputs to generate. like, As a teacher,one will be able to access all the subjects he teaches, at all the grades he teaches, which required reverse query to get all the course and subjects he teaches, As a parents one should be able to see all his/her childrens basic details, As a student one should be able to see the course and course subjects he enrolled at, so on and so forth

# Documentation

    Gradesheet
    This webapp is designed to make a automatic gradesheet out of marksheet with complex user management queries

    1. Custom User
        This app comtains custom user creation method where only the addmitted student ,appointed teacher or the student's parents can signup.If this user is not admitted or appointed one will not be able to create the account at the first place.Only the admin/staff user has permission to admit or appoint users.
    2. Role Assignment
        Each user has different role to perform and role is assigned dynamically as per database to each user while creating the account itself.
    3. Dynamic User Profile
        User with different roles will throw different API and give different Template view, all the outputs are designed as per the users requirement and needs.
