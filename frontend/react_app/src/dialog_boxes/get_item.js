import React, {useState} from "react";
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import { Button } from '@mui/material';
import { TextField } from "@mui/material";
import axios from 'axios';


const GetItemDialog = ({open, onClose, onSubmit}) => {
    const [itemId, setItemId] = useState("");
    const [itemLink, setItemLink] = useState("");
    const [message, setMessage] = useState("");


    const handleGetItem = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/get_item_link/?Item_id=${itemId}`);
            setItemLink(response.data.Link)
            setMessage("Data extracted successfully");
        } catch (error) {
            setMessage("Error: " + error.message);
        }
    };


    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>Get Item Link</DialogTitle>
            <DialogContent>
                <TextField
                    label='Item ID'
                    value={itemId}
                    onChange={(e) => setItemId(e.target.value)}
                />
                {itemLink && <a href={itemLink} terget="_blank" rel="noopener noreferrer">
                    {itemLink}
                </a>}
                {message && <p>{message}</p>}
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose}>Cancel</Button>
                <Button onClick={handleGetItem}>Get</Button>
            </DialogActions>
        </Dialog>
    );
};

export default GetItemDialog;