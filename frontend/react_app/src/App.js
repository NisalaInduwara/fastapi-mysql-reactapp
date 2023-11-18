import React, {useState} from "react";
import orders from './components/orders';
import Items from './components/items';
import disputes from './components/disputes';

function App(){
    const [activeTab, setActiveTab] = useState('home');

    const handleTabChange = (tabName) => {
        setActiveTab(tabName);
    };

    return(
        <div className="App">
            <div className="tabs">
                <button onClick={() => handleTabChange('home')} className={activeTab === 'home' ? 'active' : ''}>
                    Home page
                </button>
                <button onClick={() => handleTabChange('orders')} className={activeTab === 'orders' ? 'active' : ''}>
                    Order Data Page
                </button>
                <button onClick={() => handleTabChange('items')} className={activeTab === 'items' ? 'active' : ''}>
                    Item Data Page
                </button>
                <button onClick={() => handleTabChange('disputes')} className={activeTab === 'disputes' ? 'active' : ''}>
                    Disputes Data Page
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
