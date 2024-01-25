    async def get_form_item(self, request: Request):
        url = self.display_admin.router_path + self.display_admin.page_path
        picker = Picker(
            name=self.display_admin.model.__table__.name,
            label=self.display_admin.page_schema.label,
            labelField="name",
            valueField="id",
            multiple=True,
            required=False,
            modalMode="dialog",
            size="full",
            pickerSchema={"&": "${body}"},
            source={
                "method": "post",
                "data": "${body.api.data}",
                "url": "${body.api.url}&link_model="
                + self.pk_admin.model.__table__.name
                + "&op=in_&link_item_id=${"
                "api.qsOptions.id}",
            },
        )
        adaptor = None
        if await self.pk_admin.has_update_permission(request, None, None):
            button_create = ActionType.Ajax(
                actionType="ajax",
                label=_("Add Association"),
                level=LevelEnum.danger,
                confirmText=_("Are you sure you want to add the association?"),
                api=f"post:{self.pk_admin.app.router_path}{self.pk_admin.router.prefix}{self.path}"
                + '/${REPLACE(query.link_item_id, "!", "")}?link_id=${IF(ids, ids, id)}',
            )  # query.link_item_id
            adaptor = (
                'if(!payload.hasOwnProperty("_payload")){payload._payload=JSON.stringify(payload);}'
                "payload=JSON.parse(payload._payload);button_create="
                + button_create.amis_json()
                + ";"
                "payload.data.body.bulkActions.push(button_create);"
                "payload.data.body.itemActions.push(button_create);"
                "return payload;".replace(
                    "action_id", "create" + self.path.replace("/", "_")
                )
            )
            button_create_dialog = ActionType.Dialog(
                icon="fa fa-plus pull-left",
                label=_("Add Association"),
                level=LevelEnum.danger,
                dialog=Dialog(
                    title=_("Add Association"),
                    size="full",
                    body=Service(
                        schemaApi=AmisAPI(
                            method="post",
                            url=url,
                            data={},
                            cache=300000,
                            responseData={
                                "&": "${body}",
                                "api.url": "${body.api.url}&op=not_in&link_model="
                                + self.pk_admin.model.__table__.name
                                + "&link_item_id=${api.qsOptions.id}",
                            },
                            qsOptions={"id": f"${self.pk_admin.pk_name}"},
                            adaptor=adaptor,
                        )
                    ),
                ),
            )

            button_delete = ActionType.Ajax(
                actionType="ajax",
                label=_("Remove Association"),
                level=LevelEnum.danger,
                confirmText=_("Are you sure you want to remove the association?"),
                api=f"delete:{self.pk_admin.app.router_path}{self.pk_admin.router.prefix}{self.path}"
                + "/${query.link_item_id}?link_id=${IF(ids, ids, id)}",
            )
            adaptor = (
                'if(!payload.hasOwnProperty("_payload")){payload._payload=JSON.stringify(payload);}'
                "payload=JSON.parse(payload._payload);button_delete="
                + button_delete.amis_json()
                + ";payload.data.body.headerToolbar.push("
                + button_create_dialog.amis_json()
                + ");payload.data.body.bulkActions.push(button_delete);payload.data.body.itemActions.push(button_delete);"
                "return payload;".replace(
                    "action_id", "delete" + self.path.replace("/", "_")
                )
            )
        return Service(
            schemaApi=AmisAPI(
                method="post",
                url=url,
                data={},
                cache=300000,
                responseData={"controls": [picker]},
                qsOptions={"id": f"${self.pk_admin.pk_name}"},
                adaptor=adaptor,
            )
        )