import React, {useState} from "react";
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import { Button } from '@mui/material';
import { TextField } from "@mui/material";
import axios from 'axios';


const AddItemDialog = ({open, onClose, onSubmit}) => {
    const [itemId, setItemId] = useState("");
    const [itemLink, setItemLink] = useState("");
    const [message, setMessage] = useState("");


    const handleAddItem = async (e) => {
        e.preventDefault();
        try {
          await axios.post("http://127.0.0.1:8000/add_item/", { 
            Item_id: itemId, 
            Item_link: itemLink 
        });
          setMessage("Item added successfully.");
        } catch (error) {
          setMessage("Error: " + error.message);
        }
    };


    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>Add New Item</DialogTitle>
            <DialogContent>
                <TextField
                    label='Item ID'
                    value={itemId}
                    onChange={(e) => setItemId(e.target.value)}
                />
                <TextField
                    label='Item Link'
                    value={itemLink}
                    onChange={(e) => setItemLink(e.target.value)}
                />
                {message && <p>{message}</p>}
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose}>Cancel</Button>
                <Button onClick={handleAddItem}>Add</Button>
            </DialogActions>
        </Dialog>
    );
};

export default AddItemDialog;