open ContainersLabels

let file_is_not_empty path =
  match Aoc.Util.read_file_as_string path with
  | "" ->
      false
  | _ ->
      true
  | exception Sys_error _ ->
      false

let result_for_day (year, day) =
  let cwd = Sys.getcwd () in
  let directory = Printf.sprintf "%s/src/year_20%02d/day_%02d" cwd year day in
  if (not (Sys.file_exists directory)) || not (Sys.is_directory directory) then
    None
  else
    let path i = Printf.sprintf "%s/p%d.expected" directory i in
    let result =
      match (file_is_not_empty (path 1), file_is_not_empty (path 2)) with
      | true, false ->
          "A: *\tB: -"
      | true, true ->
          "A: *\tB: *"
      | _ ->
          "A: -\tB: -"
    in
    Some (Printf.sprintf "20%i/%02i:\t%s" year day result)

let () =
  List.(Aoc.Util.product (0 -- 99) (1 -- 25))
  |> List.filter_map ~f:result_for_day
  |> String.concat ~sep:"\n" |> print_endline
