CREATE OR REPLACE FUNCTION update_profile()
  RETURNS TRIGGER AS  $$
DECLARE
  check_id_profile integer;
  old_id_profile integer;
BEGIN
  check_id_profile = (
    with agg_d as (
select
id_user
, id_action
, count(1) c
from
              statistic_action
where id_user = new.id_user
group by id_user, id_action
)
select
id_profile
from agg_d
join action on action.id_action = agg_d.id_action
where (id_user, c) = any(select id_user, max(c) from agg_d group by id_user)
    );
  old_id_profile = (select id_profile from users where users.id_user = new.id_user);
  if old_id_profile <> check_id_profile then
    update users
      set id_profile = check_id_profile
    where id_user = new.id_user;
  end if;
  return new;
END;
$$ LANGUAGE 'plpgsql';