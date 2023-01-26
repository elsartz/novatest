import React from "react";
import axios from 'axios';

export default class Notes extends React.Component {
    constructor(props) {
        super(props);
        this.state = { notes: [] };
    }

    componentDidMount() {
        axios.get('http://localhost:5000/notes')
            .then(res => {
                this.setState({ notes: res.data });
            });
    }

    render() {
        return (
            <div className="list-group">
                {this.state.notes.map(note => (
                    <div className="list-item flex-row justify-space-between align-center" key={note.id}><h3 className="text-uppercase">{note.title}</h3>
                    <p>{note.content}</p>
                    <button className="btn icon-danger">Delete</button>
                    </div>
                    
                ))}
            </div>
        );
    }
}
