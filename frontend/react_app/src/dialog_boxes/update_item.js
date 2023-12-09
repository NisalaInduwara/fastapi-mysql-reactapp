import React, {useState} from "react";
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import { Button } from '@mui/material';
import { TextField } from "@mui/material";
import axios from 'axios';


const UpdateItemDialog = ({open, onClose, onSubmit}) => {
    const [itemId, setItemId] = useState("");
    const [itemLink, setLink] = useState("");
    const [newLink, setnewLink] = useState("");
    const [message, setMessage] = useState("");


    const handleUpdateItem = async (e) => {
        e.preventDefault();
        try {
            await axios.put(`http://127.0.0.1:8000/update_item_link/?Item_id=${itemId}&new_link=${itemLink}`);
            const response = await axios.get(`http://127.0.0.1:8000/get_item_link/?Item_id=${itemId}`);
            setMessage("Item link updated successfully to: ");
            setnewLink("Link after update: " + response.data.Link);

        } catch (error) {
            setMessage("Error: " + error.message);
        }
    };


    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>Update Item Link</DialogTitle>
            <DialogContent>
                <TextField
                    label='Item ID'
                    value={itemId}
                    onChange={(e) => setItemId(e.target.value)}
                />
                <TextField
                    label='New Link'
                    value={itemLink}
                    onChange={(e) => setLink(e.target.value)}
                />
                {message && <p>{message}</p>}
                {newLink && <a href={newLink} terget="_blank" rel="noopener noreferrer">
                    {newLink}
                </a>}
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose}>Cancel</Button>
                <Button onClick={handleUpdateItem}>Update</Button>
            </DialogActions>
        </Dialog>
    );
};

export default UpdateItemDialog;