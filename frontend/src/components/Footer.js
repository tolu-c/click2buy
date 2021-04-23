import React from "react";
import { Container, Row, Col } from "react-bootstrap";

function Footer() {
  let date = new Date();

  const currentYear = date.getFullYear();

  return (
    <footer>
      <Container>
        <Row>
          <Col className="text-center py-3">
            Copyright &copy; Click2Buy {currentYear}
          </Col>
        </Row>
      </Container>
    </footer>
  );
}

export default Footer;
