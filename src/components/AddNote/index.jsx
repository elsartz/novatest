import React from "react";
import axios from 'axios';

export default class AddNote extends React.Component {
    constructor(props) {
        super(props);
        this.state = { title: '', content: '' };
    }

    handleSubmit(e) {
        e.preventDefault();
        axios.post('http://localhost:5000/notes', {
            title: this.state.title,
            content: this.state.content
        })
            .then(res => {
                console.log(res);
                console.log(res.data);
            });
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input type="text" name="title" onChange={e => this.setState({ title: e.target.value })} />
                <textarea name="content" onChange={e => this.setState({ content: e.target.value })} />
                <button type="submit">Add Note</button>
            </form>
        );
    }
}
