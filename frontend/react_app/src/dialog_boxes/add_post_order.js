import React, {useState} from "react";
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import { Button } from '@mui/material';
import { TextField } from "@mui/material";
import axios from 'axios';


const AddPostOrderDialog = ({open, onClose, onSubmit}) => {
    const [Order_id, setOrderId] = useState("");
    const [message, setMessage] = useState("");
    const [Ali_order_id, setAliOrderID] = useState("");
    const [Tracking_number, setTrackingNumber] = useState("");
    const [NextTrackingNumber, setNextTrackingNumber] = useState("");
    const [ItemCost, setItemCost] = useState(0);


    const handleAddPostOrder = async (e) => {
        e.preventDefault();
        try{
            await axios.post("http://127.0.0.1:8000/add_post_orders/",
            {Order_id: Order_id, Ali_order_id: Ali_order_id, Tracking_number: Tracking_number,
            next_tracking_number: NextTrackingNumber, item_cost: ItemCost});
            setMessage("Post Order added successfully.");
        } catch (error){
            setMessage("Error:" + error.message);
        }
    }

    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>Add New Post Order</DialogTitle>
            <DialogContent>
                <TextField
                    label='Order ID'
                    value={Order_id}
                    onChange={(e) => setOrderId(e.target.value)}
                />
                <TextField
                    label='Ali Order ID'
                    value={Ali_order_id}
                    onChange={(e) => setAliOrderID(e.target.value)}
                />
                <TextField
                    label='Tracking Number'
                    value={Tracking_number}
                    onChange={(e) => setTrackingNumber(e.target.value)}
                />
                <TextField
                    label='Next Tracking Number'
                    value={NextTrackingNumber}
                    onChange={(e) => setNextTrackingNumber(e.target.value)}
                />
                <TextField
                    label='Item Cost'
                    value={ItemCost}
                    onChange={(e) => setItemCost(e.target.value)}
                />
                {<p>
                    <br/>
                    eBay Order ID: {Order_id}<br/>
                    Ali Order ID: {Ali_order_id}<br/>
                    Tracking Number: {Tracking_number}<br/>
                    Next Tracking Number: {NextTrackingNumber}<br/>
                    Item Cost: {ItemCost}
                    <br/>
                </p>}
                {message && <p>{message}</p>}
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose}>Cancel</Button>
                <Button onClick={handleAddPostOrder}>Add</Button>
            </DialogActions>
        </Dialog>
    );
};

export default AddPostOrderDialog;