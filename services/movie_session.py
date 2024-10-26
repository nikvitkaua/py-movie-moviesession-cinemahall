from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )

def get_movies_sessions(session_date: str = None) -> MovieSession | QuerySet:
    """
    Process a date in the format 'YYYY-MM-DD'.
    """
    if session_date:
        return MovieSession.objects.filter(show_time=session_date)

    return MovieSession.objects.all()

def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)

def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    update_fields = {}
    if show_time is not None:
        update_fields['show_time'] = show_time
    if movie_id is not None:
        update_fields['movie_id'] = movie_id
    if cinema_hall_id is not None:
        update_fields['cinema_hall_id'] = cinema_hall_id
    if update_fields:
        MovieSession.objects.filter(id=session_id).update(**update_fields)

def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
