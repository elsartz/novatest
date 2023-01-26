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
            <div>
                {this.state.notes.map(note => (
                    <div key={note.id}><h3>{note.title}</h3>
                    <p>{note.content}</p>
                    </div>
                    
                ))}
            </div>
        );
    }
}
