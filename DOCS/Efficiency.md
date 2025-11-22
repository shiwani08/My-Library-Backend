### Some Functionds modules for reusability:

    1. Use LoginManager for the login purposes
    2. Check the UserMixins for the login and user management 
    3. Use Flask-wtf for the forms 
    4. Use flask login and its functions for data validation and the the user login
    5. Check the OAuth, Flask-dance and the Flask-OAuth
    6. Use JWT tokens


1. Basics You Must Know Before CRUD

These are the warm-up stretches:

MongoDB documents & BSON

Collections vs tables

ObjectId and why it looks like a password

MongoDB shell vs Compass vs Drivers

Databases vs Collections vs Documents

Once you know these, CRUD becomes a dance.

📚 CRUD Topics (The Actual Roadmap)
📥 C – Create

insertOne()

insertMany()

Auto-generated _id

Inserting nested documents

Handling duplicates

Ordered vs unordered inserts

Extra twists worth learning:

Insert performance & writeConcern

Upserts (kind of CREATE + UPDATE)

🔍 R – Read

This is where MongoDB gets spicy.

find()

findOne()

Projection {field: 1}

Comparison operators: $gt, $lt, $eq, $ne

Logical operators: $and, $or, $not, $nor

Array queries ($in, $all, $elemMatch)

Regex search

Sorting

Pagination using limit() + skip()

Indexes (absolutely crucial for fast reads)

Deep cuts that matter in real apps:

Compound indexes

TTL indexes

Partial indexes

Text search

Case-insensitive search (collation)

✏️ U – Update

Your “editing the document” saga:

updateOne()

updateMany()

replaceOne()

$set, $unset, $rename, $inc, $push, $pull, $addToSet

Updating nested fields ("address.city": "Mumbai")

Array operators ($[], $[<identifier>])

Upserts (update or create)

Advanced:

Optimistic concurrency with $currentDate and timestamps

Schema evolution techniques

🗑️ D – Delete

Short but important:

deleteOne()

deleteMany()

drop()

Why you should never run deleteMany without a filter unless your self-esteem is dangerously high.

⚙️ Other Important MongoDB Concepts Alongside CRUD

These are not CRUD but you literally can’t build real apps without them:

Aggregation Pipeline ($match, $group, $project, $lookup)

Schema design principles (embedding vs referencing)

Data modeling patterns (bucket pattern, outlier pattern)

Transactions (multi-document ACID operations)

Connection pooling (backend-level)

Write concerns & read concerns

Index performance analysis (explain())