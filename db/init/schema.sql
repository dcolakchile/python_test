--
-- PostgreSQL database dump
--

-- Dumped from database version 14.3
-- Dumped by pg_dump version 14.2


SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 210 (class 1259 OID 16397)
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    name character varying(255),
    uom character varying(10),
    category_name character varying(255),
    is_producible boolean,
    is_purchasable boolean,
    type character varying(255),
    purchase_uom character varying(10),
    batch_tracked boolean,
    additional_info character varying(1024),
    purchase_uom_conversion_rate numeric,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    id bigint NOT NULL
);


ALTER TABLE public.product OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16406)
-- Name: productvariant; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.productvariant (
    sku character varying(30),
    sales_price numeric(16,2),
    purchase_price numeric(16,2),
    type character varying(100),
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    config_attributes json,
    id bigint NOT NULL,
    product_id bigint NOT NULL
);


ALTER TABLE public.productvariant OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16386)
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    uid uuid NOT NULL,
    username character varying(100),
    password character varying(512)
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- TOC entry 3445 (class 2606 OID 16424)
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- TOC entry 3451 (class 2606 OID 16426)
-- Name: productvariant productvariant_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productvariant
    ADD CONSTRAINT productvariant_pkey PRIMARY KEY (id);


--
-- TOC entry 3441 (class 2606 OID 16392)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (uid);


--
-- TOC entry 3446 (class 1259 OID 16434)
-- Name: fki_fk_productvariant_product_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_fk_productvariant_product_id ON public.productvariant USING btree (product_id);


--
-- TOC entry 3442 (class 1259 OID 16422)
-- Name: idx_product_category_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_product_category_name ON public.product USING btree (category_name);


--
-- TOC entry 3443 (class 1259 OID 16405)
-- Name: idx_product_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_product_name ON public.product USING btree (name);


--
-- TOC entry 3447 (class 1259 OID 16427)
-- Name: idx_productvariant_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_productvariant_id ON public.productvariant USING btree (id);


--
-- TOC entry 3448 (class 1259 OID 16428)
-- Name: idx_productvariant_product_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_productvariant_product_id ON public.productvariant USING btree (product_id);


--
-- TOC entry 3449 (class 1259 OID 16421)
-- Name: idx_productvariant_sku; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_productvariant_sku ON public.productvariant USING btree (sku);


--
-- TOC entry 3438 (class 1259 OID 16395)
-- Name: idx_user_uid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_user_uid ON public."user" USING btree (uid);


--
-- TOC entry 3439 (class 1259 OID 16396)
-- Name: idx_user_username; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_user_username ON public."user" USING btree (username);


--
-- TOC entry 3452 (class 2606 OID 16429)
-- Name: productvariant fk_productvariant_product_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productvariant
    ADD CONSTRAINT fk_productvariant_product_id FOREIGN KEY (product_id) REFERENCES public.product(id) NOT VALID;


-- Completed on 2022-09-20 14:56:38 -03

--
-- PostgreSQL database dump complete
--

