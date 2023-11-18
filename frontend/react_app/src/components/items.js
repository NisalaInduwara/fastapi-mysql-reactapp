import React, {useState} from 'react';
import axios from 'axios';

const Items = () => {
  const [itemId, setItemId] = useState("");
  const [itemLink, setItemLink] = useState("");
  const [newLink, setNewLink] = useState("");
  const [message, setMessage] = useState("");

  const handleAddItem = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://127.0.0.1:8000/add_item/", { Item_id: itemId, Item_link: itemLink });
      setMessage("Item added successfully.");
    } catch (error) {
      setMessage("Error: " + error.message);
    }
  };

  const handleGetItem = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/get_item_link/?Item_id=${itemId}`);
      setMessage("Item Link: " + response.data.Link);
    } catch (error) {
      setMessage("Error: " + error.message);
    }
  };

  const handleUpdateItem = async (e) => {
    e.preventDefault();
    try {
      await axios.put(`http://127.0.0.1:8000/update_item_link/?Item_id=${itemId}&new_link=${newLink}`);
      setMessage("Item link updated successfully.");
    } catch (error) {
      setMessage("Error: " + error.message);
    }
  };

  const handleDeleteItem = async () => {
    try {
      await axios.delete(`http://127.0.0.1:8000/delete_item/?Item_id=${itemId}`);
      setMessage("Item deleted successfully.");
    } catch (error) {
      setMessage("Error: " + error.message);
    }
  };

  return(
    <div>
      <form>
        <label>
          Item ID : 
          <input type='text' value={itemId} onChange={(e) => setItemId(e.target.value)}/>
        </label>
        <br/>
        <label>
          Item Link:
          <input type="text" value={itemLink} onChange={(e) => setItemLink(e.target.value)} />
        </label>
        <br />
        <button type="button" onClick={handleAddItem}>
          Add Item
        </button>
        <button type="button" onClick={handleGetItem}>
          Get Item
        </button>
        <button type="button" onClick={handleUpdateItem}>
          Update Item
        </button>
        <button type="button" onClick={handleDeleteItem}>
          Delete Item
        </button>
      </form>
      <div>
        <p>{message}</p>
      </div>
    </div>
  )
  

};

export default Items;