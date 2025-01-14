open ContainersLabels

let sample = {|
3   4
4   3
2   5
1   3
3   9
3   3
|} |> String.trim

let parse_lines input =
  input |> String.lines
  |> List.filter_map ~f:(Util.split_once ~on:"   ")
  |> List.map ~f:(fun (a, b) -> (int_of_string a, int_of_string b))
  |> List.split

let sort_numbers = List.sort ~cmp:(fun a b -> compare b a)

module Part_1 = struct
  let solve input =
    let left, right = parse_lines input in
    let sorted_left = sort_numbers left in
    let sorted_right = sort_numbers right in
    List.map2 sorted_left sorted_right ~f:(fun a b -> abs (a - b))
    |> List.fold_left ~f:( + ) ~init:0

  let%test "sample data" = Test.(run int (solve sample) ~expect:11)
end

module Part_2 = struct
  let solve input =
    let left, right = parse_lines input in
    List.map left ~f:(fun n ->
        n * List.length (List.filter ~f:(fun x -> x = n) right) )
    |> List.fold_left ~f:( + ) ~init:0

  let%test "sample data" = Test.(run int (solve sample) ~expect:31)
end

let run_1 () = Run.solve_int (module Part_1)

let run_2 () = Run.solve_int (module Part_2)
