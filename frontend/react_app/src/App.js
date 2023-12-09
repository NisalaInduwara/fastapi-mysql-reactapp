import React, {useState, useEffect} from "react";
import orders from './components/orders';
import Items from './components/items';
import disputes from './components/disputes';

function App(){
    const [activeTab, setActiveTab] = useState('home');

    useEffect(() => {
        const previousTab = localStorage.getItem('activateTab');
        if (previousTab){
            setActiveTab(previousTab);
        }
    }, []);

    const handleTabChange = (tabName) => {
        setActiveTab(tabName);
        localStorage.setItem('activateTab', tabName);
    };

    return(
        <div className="App">
            <div className="tabs">
                <button onClick={() => handleTabChange('home')} className={activeTab === 'home' ? 'active' : ''}>
                    Home page
                </button>
                <button onClick={() => handleTabChange('orders')} className={activeTab === 'orders' ? 'active' : ''}>
                    Orders
                </button>
                <button onClick={() => handleTabChange('items')} className={activeTab === 'items' ? 'active' : ''}>
                    Items
                </button>
                <button onClick={() => handleTabChange('disputes')} className={activeTab === 'disputes' ? 'active' : ''}>
                    Returns
                </button>
            </div>
            <div className="tab-content">
                {activeTab === 'home' &&  (
                <div>
                    <h2>Anu Stores Database System</h2>
                </div>)}

                {activeTab === 'orders' &&  (
                <div>
                    <h2>Orders Tab Content</h2>
                </div>)}

                {activeTab === 'items' && (
                <div>
                    <Items />
                </div>)}

                {activeTab === 'disputes' && (
                <div>
                    <h2>disutes Tab Content</h2>
                </div>)}
            </div>
        </div>
    );
}

export default App;
