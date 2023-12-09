import React, {useState} from "react";
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import { Button } from '@mui/material';
import { TextField } from "@mui/material";
import axios from 'axios';


const DeleteItemDialog = ({open, onClose, onSubmit}) => {
    const [itemId, setItemId] = useState("");
    const [message, setMessage] = useState("");


    const handleDeleteItem = async () => {
        try {
            await axios.delete(`http://127.0.0.1:8000/delete_item/?Item_id=${itemId}`);
            setMessage("Item deleted successfully.");
        } catch (error) {
            setMessage("Error: " + error.message);
        }
    };


    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>Delete Item Link</DialogTitle>
            <DialogContent>
                <TextField
                    label='Item ID'
                    value={itemId}
                    onChange={(e) => setItemId(e.target.value)}
                />
                {message && <p>{message}</p>}
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose}>Cancel</Button>
                <Button onClick={handleDeleteItem}>Delete</Button>
            </DialogActions>
        </Dialog>
    );
};

export default DeleteItemDialog;