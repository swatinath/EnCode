# EnCode
Objective – create, post and share blogs.

The workflow of the project is as below:
1.	User – i. Admin
           ii. Viewer
2.	Functionalities –
  2.1. Admin- 	i. login
		            ii. category (CRUD)
		            iii. blog (CRUD)
            		iv. logout
            		v. profile management
            		vi. review management

  2.2. Viewers- i. view all blogs
            		ii. view blogs category wise
            		iii. add blogs (CRUD)
            		iv. sign up
            		v. sign in
            		vi. profile management
            		vii. blog review (CR)
            		viii. logout
3.	Apps / Modules – 	i. Admin
                      ii. User (viewer)
                      iii. Blog
                      iv. Pages (Home, About, Contact)
4.	Database Tables- 	i. User (structure provided by Django)
                      ii. Category (id (PK), category )
                      iii. Blog (id (PK), category_id (FK), title, author, description, image, created_at)
                      iv. Review (id (PK), user_id (FK), rating, comment, created_at, is-visible)



