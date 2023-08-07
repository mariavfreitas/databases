-- RI1
CREATE OR REPLACE FUNCTION check_employee_age()
RETURNS TRIGGER AS
$$
BEGIN
  IF (NEW.bdate > current_date - interval '18 years') THEN
    RAISE EXCEPTION 'Employee must be at least 18 years old.';
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER employee_age_trigger
BEFORE INSERT OR UPDATE ON employee
FOR EACH ROW EXECUTE PROCEDURE check_employee_age();

-- RI2
CREATE OR REPLACE FUNCTION check_workplace_type()
RETURNS TRIGGER AS
$$
BEGIN
    IF (NEW.address NOT IN (SELECT address FROM office) AND
       NEW.address NOT IN (SELECT address FROM warehouse)) THEN
        RAISE EXCEPTION 'Address not valid.';
    END IF;

    IF (NEW.address IN (SELECT address FROM office) AND
        NEW.address IN (SELECT address FROM warehouse)) THEN
          RAISE EXCEPTION 'Address cannot be both in office and in Warehouse';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER workplace_type_trigger
BEFORE INSERT OR UPDATE ON workplace
FOR EACH ROW EXECUTE PROCEDURE check_workplace_type();

-- RI3
CREATE OR REPLACE FUNCTION check_orderno()
RETURNS TRIGGER AS
$$
BEGIN
    IF (NEW.order_no NOT IN (SELECT order_no FROM "contains")) THEN
        RAISE EXCEPTION 'Order_no doesn''t exist.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER orderno_trigger
BEFORE INSERT OR UPDATE ON "order"
FOR EACH ROW EXECUTE PROCEDURE check_orderno();
