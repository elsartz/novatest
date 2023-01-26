import React from "react";
import axios from 'axios';

export default class AddNote extends React.Component {
    constructor(props) {
        super(props);
        this.state = { title: '', content: '' };
    }

    async handleSubmit(e) {
        e.preventDefault();

        const title = document.querySelector('input[name="title"]').value;
        const content = document.querySelector('textarea[name="content"]').value;
      
        const response = await fetch(`http://localhost:5000/notes`, {
          method: 'POST',
          body: JSON.stringify({
            title,
            content
          }),
          headers: {
            'Content-Type': 'application/json'
          }
        });


        // axios.post('http://localhost:5000/notes', {
        //     title: this.state.title,
        //     content: this.state.content
        // })
        //     .then(res => {
        //         console.log(res);
        //         console.log(res.data);
        //     });
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                {/* <input type="text" name="title" onChange={e => this.setState({ title: e.target.value })} /> */}
                <input type="text" name="title" />
                {/* <textarea name="content" onChange={e => this.setState({ content: e.target.value })} /> */}
                <textarea name="content" />

                <button type="submit">Add Note</button>
            </form>
        );
    }
}
