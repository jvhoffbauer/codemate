#!/usr/bin/env python
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from strawberry.fastapi import GraphQLRouter

import aiohttp
import strawberry


# Unimplemented is an util for all the unimplemented stuff
# left here
class Unimplemented(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Unimplemented!")


#################
# API Client
# This is just a basic boilerplate to setup
#################
class Endpoint(BaseModel):
    url: str
    authorization: Optional[str] = Field(default_factory=lambda: None)

    async def exec(self, json_str: str) -> aiohttp.ClientResponse:
        headers = {
            "content-type": "application/json",
        }
        if self.authorization is not None:
            headers["authorization"] = self.authorization

        async with aiohttp.ClientSession() as session:
            return await session.post(
                url=self.url,
                data=json_str,
                headers=headers,
            )


DEFAULT_ENDPOINT = Endpoint(
    url="https://app.staging.baseten.co/applications/Vqmogn0/worklets/VBnodk0/invoke",  # noqa
    authorization="Api-Key IR5hVxK1.FlYV3hmIazD7FGvXPacQnN38wgw7CSSE",
)

MOCK_ENDPOINT = Endpoint(url="http://localhost:8001/invoke")


#################
# GRAPHQL API
# This is just a basic boilerplate to setup a graphql api backed by strawberry
# see: https://strawberry.rocks/docs for docs
#################
@strawberry.type
class Organization:
    id: str
    name: str


@strawberry.type
class Query:
    @strawberry.field
    async def organizations(self) -> List[Organization]:
        return [
            Organization(id="0", name="Baseten"),
            Organization(id="1", name="Strawberry"),
        ]

    @strawberry.field
    async def organization(self, id: str) -> Organization:
        raise Unimplemented()


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_organization(self, name: str) -> bool:
        raise Unimplemented()


SCHEMA = strawberry.Schema(Query, Mutation)


#################
# HTTP API
# This is just a basic boilerplate to setup a HTTP API using FastAPI
# see: https://fastapi.tiangolo.com/ for docs
#################

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    return """
        Welcome to baseten_take_home invoker,
        go to <a href="/graphql">/graphql</a> for the API doc
    """


# You can also remove graphql and do pure HTTP/REST/JSON endpoint
# https://fastapi.tiangolo.com/
graphql_app = GraphQLRouter(SCHEMA)
app.include_router(graphql_app, prefix="/graphql")
