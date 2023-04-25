# RestaurantAPI 

------>Product Overview
The goal of this API is to provide functionality to manage information about
available tables in a restaurant. The API will allow users to perform CRUD (Create,
Read, Update, Delete) operations on tables, including creating new tables,
retrieving information about existing tables, updating table details, and deleting
tables.

------>Target Users
The API is designed for use by restaurant owners, managers, and staff who need
to manage information about available tables in their restaurant.
Use Cases
------>The API will support the following use cases:

*Create Table: Users should be able to create new tables by providing details such as table number, seating capacity, and availability status.

*Read Table: Users should be able to retrieve information about existing tables, including table details such as table number, seating capacity, and availability status.

*Update Table: Users should be able to update table details, such as seating capacity or availability status, for existing tables.

*Delete Table: Users should be able to delete tables that are no longer needed.

Database Entities

------>Based on the requirements mentioned above, the following database entities are proposed:
● Table:
● Attributes:
● Table ID (Primary key)
● Table number (Unique)
● Seating capacity
● Availability status (e.g. Available, Reserved, Occupied)
● Created timestamp
● Updated timestamp

CRUD Endpoints

------>The API should expose the following CRUD endpoints:
● Create Table: POST /api/tables
● Read Table: GET /api/tables/:id
● Update Table: PUT /api/tables/:id
● Delete Table: DELETE /api/tables/:id

------>API Specifications

● Create Table:
	○ Endpoint: POST /api/tables
	○ Request Payload:
<code>
{
"tableNumber": "101",
"seatingCapacity": 4,
"availabilityStatus": "Available"
}
</code>
● Response
<code>
{
"id": 1,
"tableNumber": "101",
"seatingCapacity": 4,
"availabilityStatus": "Available",
"createdAt": "2023-04-14T10:00:00Z",
"updatedAt": "2023-04-14T10:00:00Z"
}
</code>
● Read Table:
	○ Endpoint: GET /api/tables/:id
	○ Response
<code>	
{
"id": 1,
"tableNumber": "101",
"seatingCapacity": 4,
"availabilityStatus": "Available",
"createdAt": "2023-04-14T10:00:00Z",
"updatedAt": "2023-04-14T10:00:00Z"
}
</code>
●  Update Table:
	○ Endpoint: PUT /api/tables/:id

Request Payload:
<code>
{
"seatingCapacity": 6,
"availabilityStatus": "Reserved"
}
</code>
● Response
<code>
{
"id": 1,
"tableNumber": "101",
"seatingCapacity": 6,
"availabilityStatus": "Reserved",
"createdAt": "2023-04-14T10:00:00Z",
"updatedAt": "2023-04-14T10:01:00Z"
}
</code>
Delete Table:
	○ Endpoint: DELETE /api/tables/:id
	○ Response
<code>
{
"id": 1,
"tableNumber": "101",
"seatingCapacity": 4,
"availabilityStatus": "Available",
"createdAt": "2023-04-14T10:00:00Z",
"updatedAt": "2023-04-14T10:00:00Z"
}
</code>
