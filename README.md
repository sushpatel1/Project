# Final Project

I have selected "Policy Enrollment" as my domain for this project. It is about People who travel internationaly and enroll for health or travel insurance. 

I have identified problem i am looking in and tried to solve it by APP's Architecture. I have created all components in the solution which is defined in Appendix A. 

# Layered Architecture
 The layered architecture design includes below elemetns:
- **Presentation Layer** 
 It has flaskapi.py file under api folder where it has API for external inputs
-  **Service layer** 
 It has handlers.py, messagebus.py and unit_of_work.py files under services folder
-  **Adapters** 
 It has repository.py, orm.py and redis_eventpublisher.py files.
-  **Domain** 
 It has commands.py, events.py and models.py

# Domain tests
-  **Unit tests**

 It has unit tests for handlers and models.
-  **Integration**
  It has test cases to test unit of work class.

# I have used below libraries for this project
- **ORM - SQLAlchemy 1.4.11**
- **Python 3.8.5**
- **Virtual Env: Final_Proj**
- **miniconda3**
- **pytest**
