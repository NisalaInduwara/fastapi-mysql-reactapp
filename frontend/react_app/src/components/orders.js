import React, {useState, useEffect} from 'react';
import axios from 'axios';
import AddPreOrderDialog from '../dialog_boxes/add_pre_order';
import AddPostOrderDialog from '../dialog_boxes/add_post_order';
import GetPreOrderDialog from '../dialog_boxes/get_item';
import { Button } from '@mui/material';

const Orders = () => {
  const [is_resolved, setIsResolved] = useState("");
  const [ali_refund, setAliRefund] = useState("")
  const [message, setMessage]  = useState("");


  const [addPreOrder, setPreOrder] = useState(false);
  const [addPostOrder, setPostOrder] = useState(false);
  const [getPreOrder, setGetPreOrder] = useState(false);

  const handleOpenAddPreOrder = () => {
    setPreOrder(true);
  }

  const handleCloseAddPreOrder = () => {
    setPreOrder(false);
  }

  const handleOpenAddPostOrder = () => {
    setPostOrder(true);
  }

  const handleCloseAddPostOrder = () => {
    setPostOrder(false);
  }

  const handleOpenGetPreOrder = () => {
    setGetPreOrder(true);
  }

  const handleCloseGetPreOrder = () => {
    setGetPreOrder(false);
  }

  return (
    <div>
      <Button variant='contained' onClick={handleOpenAddPreOrder}>
        Add Pre Order
      </Button>
      <AddPreOrderDialog
        open={addPreOrder}
        onClose={handleCloseAddPreOrder}
      />

      <Button variant='contained' onClick={handleOpenAddPostOrder}>
        Add Post Order
      </Button>
      <AddPostOrderDialog
        open={addPostOrder}
        onClose={handleCloseAddPostOrder}
      />

      <Button variant='contained' onClick={handleOpenGetPreOrder}>
        Get Pre Order
      </Button>
      <GetPreOrderDialog
        open={getPreOrder}
        onClose={handleCloseGetPreOrder}
      />
    </div>
  )

  

//  

//   const handleMakeReturnCase = async (e) => {
//     e.preventDefault();
//     try{
//       await axios.post("http://127.0.0.1:8000/make_return/", 
//       {Order_id: Order_id, is_resolved: is_resolved})
//     }catch (error){
//       setMessage("Error:" + error.message);
//     }
//   }



//   const handleGetPostOrderData = async (e) => {
//     try{
//       const response = await axios.get(`http://127.0.0.1:8000/get_postorder_data/?Order_id=${Order_id}
//       &Ali_order_id=${Ali_order_id}&Tracking_number=${Tracking_number}`)
//       setMessage(response.Order_id+'-'+response.Ali_order_id+'-'+response.Tracking_number
//       +'-'+response.next_tracking_number+'-'+response.item_cost)
//     } catch (error){
//       setMessage("Error: " + error.message);
//     }
//   }

//   const handleGetTrackingLink = async (e) => {
//     try{
//       const response = await axios.get(`http://127.0.0.1:8000/get_tracking_link/?Order_id=${Order_id}`)
//       setMessage(response.data.tracking_link)
//     }catch (error){
//       setMessage("Error: " + error.message);
//     }
//   }

//   const handleDeleteOrder = async (e) => {
//     try{
//       await axios.delete(`http://127.0.0.1:8000/delete_order/?Order_id=${Order_id}`)
//       setMessage("Order deleted successfully.");
//     }catch (error){
//       setMessage("Error: " + error.message);
//     }
//   }

//   const handleGetContactDetails = async (e) => {
//     try{
//       const response = await axios.get(`http://127.0.0.1:8000/get_contact_details/?Order_Date=${Order_Date}`)
//       setMessage(response.data)
//     }catch (error){
//       setMessage("Error: " + error.message);
//     }
//   }

//   const handleAddNextTracking = async (e) => {
//     try{
//       const response = await axios.put(`http://127.0.0.1:8000/add_next_tracking_number/
//       ?next_tracking_number=${NextTrackingNumber}&Tracking_number=${Tracking_number}`)
//       setMessage(response.data)
//     } catch (error){
//       setMessage("Error: " + error.message)
//     }
//   }

//   const handleResolveReturn = async (e) => {
//     try{
//       const response = await axios.put(`http://127.0.0.1:8000/resolve_return/?Order_id=${Order_id}
//       &ali_refund=${ali_refund}`)
//       setMessage(response.data)
//     }catch(error){
//     setMessage("Error: " + error.message)
//     }
//   }

}

export default Orders;