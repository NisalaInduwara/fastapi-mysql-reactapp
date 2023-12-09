import React, {useState, useEffect} from 'react';
import axios from 'axios';

const Orders = () => {
  const [Order_id, setOrderID] = useState("");
  const [Order_Date, setOrderDate] =  useState("");
  const [Order_Earning, setOrderEarning] = useState("");
  const [Buyer_name, setBuyerName] = useState("");
  const [Contact_number, setContactNumber] = useState("");
  const [Variation, setVariation] = useState("");
  
  const [Ali_order_id, setAliOrderID] = useState("");
  const [Tracking_number, setTrackingNumber] = useState("");
  const [NextTrackingNumber, setNextTrackingNumber] = useState("");
  const [ItemCost, setItemCost] = useState("");

  const [is_resolved, setIsResolved] = useState("");
  const [ali_refund, setAliRefund] = useState("")
  const [message, setMessage]  = useState("");

  const handleAddPreOrder = async (e) => {
    e.preventDefault();
    try{
      await axios.post("http://127.0.0.1:8000/add_pre_orders/",
      {Order_id: Order_id, Order_Date: Order_Date, Order_Earning: Order_Earning,
      Buyer_name: Buyer_name, Contact_number: Contact_number, Variation: Variation});
      setMessage("Order added successfully.");
    } catch (error){
      setMessage("Error:" + error.message);
    }
  }

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

  const handleMakeReturnCase = async (e) => {
    e.preventDefault();
    try{
      await axios.post("http://127.0.0.1:8000/make_return/", 
      {Order_id: Order_id, is_resolved: is_resolved})
    }catch (error){
      setMessage("Error:" + error.message);
    }
  }

  const handleGetPreOrderData = async (e) => {
    e.preventDefault();
    try{
      const response = await axios.get(`http://127.0.0.1:8000/get_preorder_data/?Order_id=${Order_id}`)
      setMessage(response.Order_id + '-' + response.Order_Date + '-' + response.Order_Earning
      + '-' + response.Buyer_name + '-' + response.Contact_number + '-' + response.Variation);
    } catch (error) {
      setMessage("Error: " + error.message);
    }
  }

  const handleGetPostOrderData = async (e) => {
    try{
      const response = await axios.get(`http://127.0.0.1:8000/get_postorder_data/?Order_id=${Order_id}
      &Ali_order_id=${Ali_order_id}&Tracking_number=${Tracking_number}`)
      setMessage(response.Order_id+'-'+response.Ali_order_id+'-'+response.Tracking_number
      +'-'+response.next_tracking_number+'-'+response.item_cost)
    } catch (error){
      setMessage("Error: " + error.message);
    }
  }

  const handleGetTrackingLink = async (e) => {
    try{
      const response = await axios.get(`http://127.0.0.1:8000/get_tracking_link/?Order_id=${Order_id}`)
      setMessage(response.data.tracking_link)
    }catch (error){
      setMessage("Error: " + error.message);
    }
  }

  const handleDeleteOrder = async (e) => {
    try{
      await axios.delete(`http://127.0.0.1:8000/delete_order/?Order_id=${Order_id}`)
      setMessage("Order deleted successfully.");
    }catch (error){
      setMessage("Error: " + error.message);
    }
  }

  const handleGetContactDetails = async (e) => {
    try{
      const response = await axios.get(`http://127.0.0.1:8000/get_contact_details/?Order_Date=${Order_Date}`)
      setMessage(response.data)
    }catch (error){
      setMessage("Error: " + error.message);
    }
  }

  const handleAddNextTracking = async (e) => {
    try{
      const response = await axios.put(`http://127.0.0.1:8000/add_next_tracking_number/
      ?next_tracking_number=${NextTrackingNumber}&Tracking_number=${Tracking_number}`)
      setMessage(response.data)
    } catch (error){
      setMessage("Error: " + error.message)
    }
  }

  const handleResolveReturn = async (e) => {
    try{
      const response = await axios.put(`http://127.0.0.1:8000/resolve_return/?Order_id=${Order_id}
      &ali_refund=${ali_refund}`)
      setMessage(response.data)
    }catch(error){
    setMessage("Error: " + error.message)
    }
  }

}

export default Orders;