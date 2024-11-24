# from fastapi import APIRouter, HTTPException, status

# router = APIRouter()

# items = []
# item_id_counter = 1

# @router.get("/items")
# def get_items():
#     return items

# @router.post("/items", status_code=status.HTTP_201_CREATED)
# def create_item(item: Item):
#     global item_id_counter
#     item_data = item.dict()
#     item_data['id'] = item_id_counter
#     items.append(item_data)
#     item_id_counter += 1
#     return item_data

# @router.get("/items/{item_id}")
# def get_item(item_id: int):
#     for item in items:
#         if item['id'] == item_id:
#             return item
#     raise HTTPException(status_code=404, detail="Item not found")

# @router.put("/items/{item_id}")
# def update_item(item_id: int, item_update: dict):
#     for i, item in enumerate(items):
#         if item['id'] == item_id:
#             items[i].update(item_update)
#             return items[i]
#     raise HTTPException(status_code=404, detail="Item not found")

# @router.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     for i, item in enumerate(items):
#         if item['id'] == item_id:
#             del items[i]
#             return {"message": "Item deleted"}
#     raise HTTPException(status_code=404, detail="Item not found")
