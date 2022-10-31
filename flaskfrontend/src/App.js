import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Header from "./components/Header";
import Search from "./components/search";
import ImagCard from "./components/ImageCard";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5050';

const App = () => {
  const [word, setWord] = useState('');
  const [images, setImages] = useState([]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    fetch(
      `${API_URL}/newimg?query=${word}`
    )
      .then((res) => res.json())
      .then((data) => {
        setImages([{...data, title: word }, ...images]);
        
      })
      .catch((err) => {
        console.log(err);
      });
    setWord('');
  };

  const handleDeleteImage = (id) => {
    setImages(images.filter((image) => image.id !== id ));
  };

  return (
    <div className="App">
      <Header title="Images Gallery" />
      <Search word={word} setWord={setWord} handleSubmit={handleSearchSubmit} />
      <Container className="mt-4">
         <Row xs={1} md={2} lg={3}>
          {images.map((image, i) => <Col key ={i} className='pb-3'> <ImagCard  image = {image} deleteImage = {handleDeleteImage}/>
          </Col>
          )}
          </Row> 
        </Container>
    </div>
  );
};
export default App;
