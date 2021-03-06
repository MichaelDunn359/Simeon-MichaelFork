COMP3207 second coursework

# API Specification
All calls are within the /api dir in the format. comp3207.brooks107.me/api/[area]/[action]. The calls are all POST only and all return JSON with the specifed variables. 

## api/room
This area is concerned with managing the rooms (or whiteboards).

### api/room/create
Input:
 - User's name [creator::string] - This is the display name of the user who is creating the room
 - Allow others to edit [editable::bool] - If true then is a student-student model otherwise is teacher-student model

Output:
 - Room passcode [passcode::string] - This is a human readable word to be shared with other users to connect to the room
 - User auth token [token::string] - This is not for sharing and should be sent by the client for all further requests in the room

### api/room/join
Input:
 - Room passcode [passcode::string] - This is the human readable word given by the room creator and then inputted by the current user
 - User's name [name::string] - This is the display name of the user who is currently logging in

Output:
 - User auth token [token::string] - This is not for sharing and should be sent by the client for all further requests in the room



## api/graphic
This area is concerned with managing the graphics on a specific whiteboard.

### api/graphics/add
Input:
 - Auth token [token::string] - This identifies and authenticates the user to the whiteboard
 - Serialized graphic [graphic::json] - This is the graphic information that is generated by fabric.js + anything extra. The client shold accept anything in the retrieve call

Output:
 - Time of writing graphic [drawTime::long (UNIX time)] - This is the exact time that the datastore was written with the new graphic

### api/graphics/retrieve
Input:
 - Auth token [token::string] - This identifies and authenticates the user to the whiteboard
 - Time of last refres [time::long (UNIX time)] - This is the time of the oldest graphic to retrieve (to allow partical retrieves). Can be null to fetch all graphics

Output:
 - Array of serialized graphics [graphic[]::json] - This is an array of the graphics written since the time given. Maybe 0 length
 - Time of retrieval [time::long (UNIX time)] - The time that the graphics were recieved (to be passed to the next refresh request)

### api/graphics/wait (Long polling)
Input:
 - Auth token [token::string] - This identifies and authenticates the user to the whiteboard
 - Max waiting time [timeout::long (ms)] - This is the longest that the request will wait before returning something

Output:
 - New graphics available [changed::bool] - If true then new graphics have been added since the request was made, otherwise the timeout was reached



## api/chat
This area will be for a chat room system, but this will likely be dealt with by a library, and is definately further down the line so is blank for now