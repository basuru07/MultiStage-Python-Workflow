from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
data_store = {}
id_counter = 1

# Create
@app.route('/items', methods=['POST'])
def create_item():
    global id_counter
    item = request.json
    item['id'] = id_counter
    data_store[id_counter] = item
    id_counter += 1
    return jsonify(item), 201

# Read All
@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(list(data_store.values()))

# Read One
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = data_store.get(item_id)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Update
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id in data_store:
        updated_data = request.json
        updated_data['id'] = item_id
        data_store[item_id] = updated_data
        return jsonify(updated_data)
    return jsonify({'error': 'Item not found'}), 404

# Delete
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in data_store:
        deleted = data_store.pop(item_id)
        return jsonify(deleted)
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
