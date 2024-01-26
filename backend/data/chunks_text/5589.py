- This method is asynchronous and takes one or more item IDs as arguments (stored in a tuple `item_id`) of type string. - It returns a list of TableModelT objects containing the fetched database data for the specified items. - The actual query execution is delegated to an internal helper function _fetch_item_scalars using the AsyncIOMotor's runSync() method which blocks until the operation completes synchronously.