import React, {useState} from "react";
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import { Button } from '@mui/material';
import { TextField } from "@mui/material";
import axios from 'axios';


const GetPreOrderDialog = ({open, onClose, onSubmit}) => {
    const [Order_id, setOrderId] = useState("");
    const [Order_Date, setOrderDate] = useState("");
    const [Order_Earning, setEarning] = useState(0);
    const [Buyer_name, setBuyer] = useState("");
    const [Contact_number, setContactNumber] = useState("");
    const [Variation, setVariation] = useState("");
    const [message, setMessage] = useState("");


    const handleGetPreOrderData = async (e) => {
        e.preventDefault();
        try{
            const response = await axios.get(`http://127.0.0.1:8000/get_preorder_data/?Order_id=${Order_id}`)
            setMessage("Data Extracted Successfully")
            setOrderDate(response.Order_Date)
            setEarning(response.Order_Earning)
            setBuyer(response.Buyer_name)
            setContactNumber(response.Contact_number)
            setVariation(response.Variation)
        } catch (error) {
            setMessage("Error: " + error.message);
        }
  }

    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>Get Pre Order</DialogTitle>
            <DialogContent>
                <TextField
                    label='Order ID'
                    value={Order_id}
                    onChange={(e) => setOrderId(e.target.value)}
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
                <Button onClick={handleGetPreOrderData}>Get</Button>
            </DialogActions>
        </Dialog>
    );
};

export default GetPreOrderDialog;