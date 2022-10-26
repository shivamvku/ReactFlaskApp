import React from "react";
import { Navbar, Container } from 'react-bootstrap';
import { ReactComponent as Logo } from '../images/logo.svg';

const navbarStyle = {
  backgroundColor: 'Lightblue'
};
const Header = ({title}) => {
    return(
        <Navbar style={navbarStyle} variant="light">
          <Container>
            <Logo alt = {title} style = {{ maxWith: '100rem', maxHeight:'6rem'}} />
          </Container>
      </Navbar>
    )
};

export default Header;