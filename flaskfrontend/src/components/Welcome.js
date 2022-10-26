import React from "react";
import { Jumbotron, Button} from 'react-bootstrap';

const Welcome = () => {

<Jumbotron>
  <h1>Images Gallery</h1>
  <p>
    This is a simple application that retrives photos from unsplash api. In order to start enter any search term in the input feild.  </p>
  <p>
    <Button variant="primary" href = "https://unsplash.com" target="_blank"> Learn more
    
     </Button>
  </p>
</Jumbotron>;

};

export default Welcome;