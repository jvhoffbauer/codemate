"""
For Admin API : 검수
"""
from datetime import datetime, timedelta
from typing import Any, Optional, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.utils.api.admin import manager_name_extract, warning_level_changer
from app import crud
from app.schemas.admin.monitoring import (MonthlyData, MonthlyStatistic,
                                          MonitoringTableRow, MonitoringTablePage,
                                          SeriesDetail, SeriesStatusEdit)
from app.controllers import deps
from app.utils.api.novel import get_meta_from_meta_list

router = APIRouter()


@router.get("/statistic", response_model=MonthlyStatistic)
def get_monitoring_statistic(
        *,
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    어드민 > 모니터링의 월별 누적 현황을 리턴합니다.\n
    month: 1 > 이번달\n
    month: 2 > 이전달\n
    month: 3 > 전전달
    """
    series_list = crud.series_status.get_all(db=db)

    total = len(series_list)

    # 필터 함수를 위한 시간대 설정
    now_month = datetime.now().month
    this_month_end = (datetime.now() + timedelta(hours=9)).replace(month=now_month + 1, day=1, hour=0, minute=0, second=0)
    this_month_start = (datetime.now() + timedelta(hours=9)).replace(day=1, hour=0, minute=0, second=0)
    prev_month_start = (datetime.now() + timedelta(hours=9)).replace(month=now_month - 1, day=1, hour=0, minute=0, second=0)
    preprev_month_start = (datetime.now() + timedelta(hours=9)).replace(month=now_month - 2, day=1, hour=0, minute=0, second=0)

    # 등록건수 확인 > 이번달 시작일 ~ 이번달 종료일 사이에 생성된 시리즈 정보
    this_month_registered = list(
        filter(lambda series: this_month_start <= series.created_at + timedelta(hours=9) < this_month_end,
               [series for series in series_list]))

    # 처리건수 확인 > 이번달 시작일 ~ 이번달 종료일 사이에 상태 변경된 시리즈 정보
    this_month_processed = list(
        filter(lambda series:
               this_month_start <= series.updated_at + timedelta(hours=9) < this_month_end and series.status == "APPROVED",
               [series for series in series_list]))

    # 누적 미처리건 > 전체 미처리건 정보
    this_month_unprocessed = list(
        filter(lambda series: series.status == "UNAPPROVED",
               [series for series in series_list]))

    prev_month_registered = list(
        filter(lambda series: prev_month_start <= series.created_at + timedelta(hours=9) < this_month_start,
               [series for series in series_list]))

    prev_month_processed = list(
        filter(lambda series:
               prev_month_start <= series.updated_at + timedelta(hours=9) < this_month_start and series.status == "APPROVED",
               [series for series in series_list]))

    prev_month_unprocessed = list(
        filter(lambda series:
               series.updated_at + timedelta(hours=9) < this_month_start and series.status == "UNAPPROVED",
               [series for series in series_list]))

    preprev_month_registered = list(
        filter(lambda series: preprev_month_start <= series.created_at + timedelta(hours=9) < prev_month_start,
               [series for series in series_list]))

    preprev_month_processed = list(
        filter(lambda series:
               preprev_month_start <= series.updated_at + timedelta(hours=9) < prev_month_start and series.status == "APPROVED",
               [series for series in series_list]))

    preprev_month_unprocessed = list(
        filter(lambda series:
               series.updated_at + timedelta(hours=9) < prev_month_start and series.status == "UNAPPROVED",
               [series for series in series_list]))

    this_month = MonthlyData(
        month=1,
        registered=len(this_month_registered),
        processed=len(this_month_processed),
        unprocessed=len(this_month_unprocessed)
    )

    prev_month = MonthlyData(
        month=2,
        registered=len(prev_month_registered),
        processed=len(prev_month_processed),
        unprocessed=len(prev_month_unprocessed)
    )

    preprev_month = MonthlyData(
        month=3,
        registered=len(preprev_month_registered),
        processed=len(preprev_month_processed),
        unprocessed=len(preprev_month_unprocessed)
    )

    return MonthlyStatistic(total=total, detail=[this_month, prev_month, preprev_month])


@router.get("/table", response_model=MonitoringTablePage)
def get_monitoring_table(
        q: Optional[str] = None,
        region_code: Optional[str] = None, created_from: Optional[str] = "2000-02-22T09:00", created_to: Optional[str] = "2999-02-22T09:00", status: Optional[str] = None,
        *, db: Session = Depends(deps.get_db), page_request: dict = Depends(deps.get_page_request),
        ) -> Any:
    """
    어드민 > 모니터링의 테이블에 들어갈 데이터를 리턴합니다. query_params가 없을경우 (ex. /table?region_code=q=) 전체를 리턴합니다.
    """
    raw_data = jsonable_encoder(crud.series_status.get_list_paginated_for_admin(db=db, page_request=page_request, q=q, region_code=region_code, created_from=created_from, created_to=created_to, status=status))
    detail_data = raw_data.get("content")
    page_meta = raw_data.get("page_meta")

    detail_data_list = [MonitoringTableRow(
        id=data.get("id"),
        series_id=data.get("series").get("id"),
        status=data.get("status"),
        title=get_meta_from_meta_list(meta_list=data.get("series").get("novel").get("novel_meta"),
                                      comparison="is_origin", criteria=True, value="title"),
        series=f"{data.get('series').get('order_number')}: "
               f"{get_meta_from_meta_list(meta_list=data.get('series').get('series_meta'), comparison='is_origin', criteria=True, value='title')}",
        writer_nickname=data.get("series").get("novel").get("writer_nickname"),
        region_code=data.get("series").get("novel").get("region_code"),
        created_at=data.get("created_at"),
        processed_at=data.get("updated_at"),
        manager=manager_name_extract(data.get("manager"))
    ) for data in detail_data]

    return MonitoringTablePage(page_meta=page_meta, contents=detail_data_list)


@router.get("/{series_status_id}", response_model=SeriesDetail)
def get_series_detail(
        *,
        db: Session = Depends(deps.get_db),
        series_status_id: int
) -> Any:
    """
    어드민 > 모니터링 > 테이블의 각 회차 > 해당 회차 상세정보 \n
    path_parameter로 "series_status_id"를 받습니다. series_status_id 는 /admin/table [GET]을 통해 받는 회차 상태 정보의 __"series_id"가 아닌, "id" 값 입니다.__
    """
    series = crud.series_status.get(db=db, id=series_status_id)
    series_data_raw = jsonable_encoder(crud.series.get_detail(db=db, id=series.series_id))
    series_data = SeriesDetail(
        id=series_data_raw.get("id"),
        status=series_data_raw.get("status"),
        title=get_meta_from_meta_list(meta_list=series_data_raw.get("novel").get("novel_meta"), comparison="is_origin", criteria=True, value="title"),
        series=f"{series_data_raw.get('order_number')}: "
               f"{get_meta_from_meta_list(meta_list=series_data_raw.get('series_meta'), comparison='is_origin', criteria=True, value='title')}",
        writer_nickname=series_data_raw.get("novel").get("writer_nickname"),
        region_code=series_data_raw.get("novel").get("region_code"),
        created_at=series_data_raw.get("created_at"),
        is_censored=series_data_raw.get("novel").get("is_censored"),
        contents=[paragraph.get("text") for paragraph in series_data_raw.get("paragraph")]
    )
    return series_data


@router.post("/{series_status_id}")
def edit_series_status(
        *,
        db: Session = Depends(deps.get_db),
        series_status_id: int,
        series_status_in: SeriesStatusEdit
) -> Any:
    """
    :param series_status_id: series_status_id 는 /admin/table [GET]을 통해 받는 회차 상태 정보의 __"series_id"가 아닌, "id" 값 입니다.__\n
    :param reason: https://docs.google.com/spreadsheets/d/1zYQQe16VIXbP-5dHwbIG7u-3uHJrO_qUpccOf3_g-9E/edit#gid=1243584415 "노출제한사유" 탭의 코드값을 인자로 받습니다.
    """
    series_status_data = crud.series_status.get_detail(db=db, id=series_status_id)
    json_series_status_data = jsonable_encoder(series_status_data)

    # 관리 사항 반영을 위해 시리즈 (노출 중단 적용), 회원 (경고 적용) ID 조회
    series_id = json_series_status_data.get("series").get("id")
    user_id = json_series_status_data.get("series").get("writer").get("user").get("id")

    # 삭제일 경우 바로 삭제
    if series_status_in.is_delete is True:
        crud.series.delete_by_monitoring(db=db, id=series_id)
        return "deleted"

    # 수정사항 반영을 위해 수정사항 반영할 회차 / 회원 데이터 조회
    series_data = crud.series.get(db=db, id=series_id)
    user_data = crud.user.get(db=db, id=user_id)

    '''
    수정사항 반영 로직
    '''
    # 선택값에 맞게 노출 상태 변경 // 알람 가는 기능 구현 필요
    crud.series.update(db=db,
                       db_obj=series_data,
                       obj_in={"status": "APPROVED", "is_impressing": series_status_in.is_impressing})

    # 경고가 있다면 유저 경고 추가 // 알람 가는 기능 구현 필요
    if series_status_in.is_warning is True:
        crud.user.update(db=db,
                         db_obj=user_data,
                         obj_in={"status": warning_level_changer(user_data.status)})

    # 어떤 행위를 하든 이 함수가 요청되면 시리즈 상태 테이블을 무조건 처리 상태로 변경 (7/13 오후 협의된 사항)
    series_status_data.reason = series_status_in.reason
    series_status_data.status = "APPROVED"
    series_status_data.manager_id = 3   # 로그인 구현 후 수정할 부분
    db.commit()
    db.refresh(series_status_data)

    return series_status_data


@router.post("/{series_status_id}/check")
def check_series_status(
        *,
        db: Session = Depends(deps.get_db),
        series_status_id: int
) -> Any:
    """
    path_parameter로 "series_status_id"를 받습니다. series_status_id 는 /admin/table [GET]을 통해 받는 회차 상태 정보의 __"series_id"가 아닌, "id" 값 입니다.__\n
    해당 "시리즈 상태"를 확인했다는 뜻으로, 어드민 > 모니터링 > 회차 상세정보에서 "승인"버튼 클릭과 이어지는 API
    """

    series_status_data = crud.series_status.get_detail(db=db, id=series_status_id)
    series_data = crud.series.get(db=db, id=series_status_data.series_id)
    crud.series.update(db=db, db_obj=series_data, obj_in={"status": "APPROVED"})

    # 로그인 구현 되면, obj_in 의 파라미터에 수정한 사람 작성 필요
    series_status_data.reason = "NORMAL"
    series_status_data.status = "APPROVED"
    series_status_data.manager_id = 3  # 로그인 구현 후 수정할 부분
    db.commit()
    db.refresh(series_status_data)

    return series_status_data
