import React, {useState, useEffect} from 'react';
import axios from 'axios';

const Items = () => {
  const [itemId, setItemId] = useState("");
  const [itemLink, setItemLink] = useState("");
  const [message, setMessage] = useState("");
  const [ID, setID] = useState("")
  const [Link, setLink] = useState("");
  const [newLink, setnewLink] = useState("");
  const [items, setItems] = useState("");


  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/items/');
        console.log(response.data);
        setItems(response.data);
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    };

    fetchItems();
  }, []);


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
      const old_response = await axios.get(`http://127.0.0.1:8000/get_item_link/?Item_id=${itemId}`);
      await axios.put(`http://127.0.0.1:8000/update_item_link/?Item_id=${itemId}&new_link=${itemLink}`);
      const new_response = await axios.get(`http://127.0.0.1:8000/get_item_link/?Item_id=${itemId}`);
      setMessage("Item link updated successfully.");
      setLink("Link before update: " + old_response.data.Link);
      setnewLink("Link after update: " + new_response.data.Link);

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

  const isItemsEmpty = items.length === 0;

  const rendered_Form = (
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
  )

  return (
    <div>
      {rendered_Form}
      <div>
        {isItemsEmpty ? (
          <p>Loading .....</p>
        ):(
          <ul>
          {items.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
        )}
      <div>
      </div>
        <div><p>{message}</p></div>
        <div><p>{ID}</p></div>
        <div><p>{Link}</p></div>
        <div><p>{newLink}</p></div>
      </div>
    </div>
  )
};

export default Items;