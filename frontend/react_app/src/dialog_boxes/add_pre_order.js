import React, {useState} from "react";
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import { Button } from '@mui/material';
import { TextField } from "@mui/material";
import axios from 'axios';


const AddPreOrderDialog = ({open, onClose, onSubmit}) => {
    const [Order_id, setOrderId] = useState("");
    const [Order_Date, setOrderDate] = useState("");
    const [Order_Earning, setEarning] = useState(0);
    const [Buyer_name, setBuyer] = useState("");
    const [Contact_number, setContactNumber] = useState("");
    const [Variation, setVariation] = useState("");
    const [message, setMessage] = useState("");


    const handleAddPreOrder = async (e) => {
        e.preventDefault();
        try{
          await axios.post("http://127.0.0.1:8000/add_pre_orders/",
          {Order_id: Order_id, Order_Date: Order_Date, Order_earning: Order_Earning,
          Buyer_name: Buyer_name, Contact_number: Contact_number, variation: Variation});
          setMessage("Order added successfully.");
        } catch (error){
          setMessage("Error:" + error.message);
        }
    }

    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>Add New Pre Order</DialogTitle>
            <DialogContent>
                <TextField
                    label='Order ID'
                    value={Order_id}
                    onChange={(e) => setOrderId(e.target.value)}
                />
                <TextField
                    label='Order ID'
                    value={Order_Date}
                    onChange={(e) => setOrderDate(e.target.value)}
                />
                <TextField
                    label='Order Earning'
                    value={Order_Earning}
                    onChange={(e) => setEarning(e.target.value)}
                />
                <TextField
                    label='Buyer Name'
                    value={Buyer_name}
                    onChange={(e) => setBuyer(e.target.value)}
                />
                <TextField
                    label='Contact Number'
                    value={Contact_number}
                    onChange={(e) => setContactNumber(e.target.value)}
                />
                <TextField
                    label='Variation'
                    value={Variation}
                    onChange={(e) => setVariation(e.target.value)}
                />
                {<p>
                    <br/>
                    eBay Order ID: {Order_id}<br/>
                    Order Date: {Order_Date}<br/>
                    Order Earning: {Order_Earning}<br/>
                    Buyer: {Buyer_name}<br/>
                    Contact Number: {Contact_number}<br/>
                    Variation: {Variation}
                    <br/>
                </p>}
                {message && <p>{message}</p>}
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose}>Cancel</Button>
                <Button onClick={handleAddPreOrder}>Add</Button>
            </DialogActions>
        </Dialog>
    );
};

export default AddPreOrderDialog;