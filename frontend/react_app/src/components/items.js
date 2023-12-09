import React, {useState, useEffect} from 'react';
import axios from 'axios';
import { Button } from '@mui/material';
import AddItemDialog from '../dialog_boxes/add_item';
import GetItemDialog from '../dialog_boxes/get_item';
import UpdateItemDialog from '../dialog_boxes/update_item';
import DeleteItemDialog from '../dialog_boxes/delete_item';

const Items = () => {
  const [items, setItems] = useState([]);
  const [addItemDialog, setAddItem] = useState(false);
  const [getItemDialog, setGetItem] = useState(false);
  const [updateItemDialog, setUpdateItem] = useState(false);
  const [deleteItemDialog, setDeleteItem] = useState(false);


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


  const handleOpenAddItem = () => {
    setAddItem(true);
  }

  const handleCloseAddItem = () => {
    setAddItem(false);
  }

  const handleOpenGetItem = () => {
    setGetItem(true);
  }

  const handleCloseGetItem = () => {
    setGetItem(false);
  }

  const handleOpenUpdateItem = () => {
    setUpdateItem(true);
  }

  const handleCloseUpdateItem = () => {
    setUpdateItem(false);
  }

  const handleOpenDeleteItem = () => {
    setDeleteItem(true);
  }

  const handleCloseDeleteItem = () => {
    setDeleteItem(false);
  }

  const isItemsEmpty = items.length === 0;

  return (
    <div>
      <div>
        <Button variant='contained' onClick={handleOpenAddItem}>
          Add Item
        </Button>
        <AddItemDialog
          open={addItemDialog}
          onClose={handleCloseAddItem}
        />

        <Button variant='contained' onClick={handleOpenGetItem}>
          Get Item Link
        </Button>
        <GetItemDialog
          open={getItemDialog}
          onClose={handleCloseGetItem}
        />

        <Button variant='contained' onClick={handleOpenUpdateItem}>
          Update Item Link
        </Button>
        <UpdateItemDialog
          open={updateItemDialog}
          onClose={handleCloseUpdateItem}
        />

        <Button variant='contained' onClick={handleOpenDeleteItem}>
          Delete Item
        </Button>
        <DeleteItemDialog
          open={deleteItemDialog}
          onClose={handleCloseDeleteItem}
        />
        
      </div>
        {isItemsEmpty ? (
          <p>Loading .....</p>
        ):(
          <ul>
          {items.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
        )}
    </div>
  )
};

export default Items;
