# metsenat_api

Metsenat API Links:

SPONSOR:
* api/v1/users/sponsors/  ➟  SPONSORS LIST (GET)
* api/v1/users/sponsors/register/  ➟  REGISTER SPONSOR (POST)
* api/v1/users/sponsors/<int:pk>/  ➟  SPONSOR DETAIL, UPDATE, DELETE (GET, PUT, PATCH, DELETE)<br>
filters:
* api/v1/users/sponsors/?search=  ➟  SEARCH BY full_name, phone_number (GET)
* api/v1/users/sponsors/?status=  ➟  FILTER BY status (GET)
* api/v1/users/sponsors/?total_money=  ➟  FILTER BY total_money (GET)
* api/v1/users/sponsors/?create_at=  ➟  FILTER BY create_at (GET)


UNIVERSITY:
* api/v1/users/university/  ➟  UNIVERSITY LIST, CREATE (GET, POST)


STUDENT:
* api/v1/users/students/create/  ➟  STUDENT CREATE (POST)
* api/v1/users/students/  ➟  STUDENTS LIST (GET)
* api/v1/users/students/<int:pk>/  ➟  STUDENT DETAIL, DELETE (GET, DELETE)
* api/v1/users/students/<int:pk>/update/  ➟  STUDENT UPDATE (PUT, PATCH) <br>
filters:
* api/v1/users/students/?search=  ➟  SEARCH BY full_name, phone_number (GET)
* api/v1/users/students/?student_type=  ➟  FILTER BY student_type (GET)
* api/v1/users/students/?university=  ➟  FILTER BY university (GET)


SPONSOR_STUDENT:
* api/v1/sponsorship/  ➟  STUDENT_SPONSORS LIST (GET)
* api/v1/sponsorship/create/  ➟  STUDENT_SPONSORS CREATE (POST)
* api/v1/sponsorship/<int:pk>/  ➟  STUDENT_SPONSORS DETAIL, DELETE (GET, DELETE)
* api/v1/sponsorship/<int:pk>/update/  ➟  STUDENT_SPONSORS UPDATE (PUT, PATCH) <br>
filters:
* api/v1/users/sponsorship/?amount=  ➟  FILTER BY amount (GET)


DASHBOARD:
* api/v1/sponsorship/dashboard/overall-statistics/  ➟  GIVEN RECIEVED MONEY STATISTICS (GET)
* api/v1/sponsorship/dashboard/sponsors/  ➟  STUDENTS STATISTICS LIST (GET)
* api/v1/sponsorship/dashboard/students/  ➟  SPONSORS STATISTICS LIST (GET)

